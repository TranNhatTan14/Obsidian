import os
import re
from collections import defaultdict
import pandas as pd
from typing import Dict, Set, List
import string

class MarkdownVocabularyAnalyzer:
    def __init__(self):
        self.word_data = defaultdict(lambda: {'frequency': 0, 'files': set()})
        self.ignored_words = set()  # You can add common words to ignore here
        
    def load_markdown_file(self, filepath: str) -> str:
        """Read content from a markdown file."""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file {filepath}: {str(e)}")
            return ""

    def clean_text(self, text: str) -> str:
        """Clean markdown text by removing code blocks, links, and special characters."""
        # Remove code blocks
        text = re.sub(r'```[\s\S]*?```', '', text)
        text = re.sub(r'`[^`]*`', '', text)
        
        # Remove URLs and image references
        text = re.sub(r'\[([^\]]*)\]\([^\)]*\)', r'\1', text)
        text = re.sub(r'!\[([^\]]*)\]\([^\)]*\)', '', text)
        
        # Remove HTML tags
        text = re.sub(r'<[^>]*>', '', text)
        
        # Remove special characters and convert to lowercase
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        
        return text

    def extract_words(self, text: str) -> List[str]:
        """Extract individual words from cleaned text."""
        words = text.split()
        # Filter out numbers and single characters
        return [word for word in words 
                if not word.isdigit() 
                and len(word) > 1 
                and word not in self.ignored_words]

    def process_file(self, filepath: str):
        """Process a single markdown file and update word frequencies."""
        content = self.load_markdown_file(filepath)
        if not content:
            return
        
        cleaned_text = self.clean_text(content)
        words = self.extract_words(cleaned_text)
        
        for word in words:
            self.word_data[word]['frequency'] += 1
            self.word_data[word]['files'].add(filepath)

    def scan_directory(self, directory: str):
        """Recursively scan directory for markdown files."""
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.md'):
                    filepath = os.path.join(root, file)
                    self.process_file(filepath)

    def generate_report(self, output_file: str):
        """Generate CSV report with word frequencies and file paths."""
        # Convert data to format suitable for DataFrame
        rows = []
        for word, data in self.word_data.items():
            rows.append({
                'word': word,
                'frequency': data['frequency'],
                # 'file_paths': '|'.join(sorted(data['files']))
            })
        
        # Create DataFrame and sort by frequency
        df = pd.DataFrame(rows)
        df = df.sort_values('frequency', ascending=False)
        
        # Save to CSV
        df.to_csv(output_file, index=False)
        print(f"Report generated successfully: {output_file}")
        
        # Print summary statistics
        print(f"\nTotal unique words analyzed: {len(df)}")
        print(f"Top 10 most frequent words:")
        print(df.head(10)[['word', 'frequency']].to_string())

def main():
    # Get directory path from user
    directory = input("Enter the directory path to analyze: ")
    output_file = "vocabulary_analysis.csv"
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    analyzer = MarkdownVocabularyAnalyzer()
    print(f"Analyzing markdown files in {directory}...")
    analyzer.scan_directory(directory)
    analyzer.generate_report(output_file)

if __name__ == "__main__":
    main()