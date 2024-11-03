import os
import re
from collections import defaultdict
import pandas as pd
from typing import Dict, Set, List
import string
from datetime import datetime, timedelta

class MarkdownVocabularyAnalyzer:
    def __init__(self):
        self.word_data = defaultdict(lambda: {
            'frequency': 0, 
            'files': set(),
            'first_seen_date': None,
            'is_new': False
        })
        self.ignored_words = set()
        self.cutoff_date = datetime.now() - timedelta(days=30)
        
    def load_markdown_file(self, filepath: str) -> tuple[str, datetime]:
        """Read content from a markdown file and get its modification time."""
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
            mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))
            return content, mod_time
        except Exception as e:
            print(f"Error reading file {filepath}: {str(e)}")
            return "", None

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
        content, mod_time = self.load_markdown_file(filepath)
        if not content or not mod_time:
            return
        
        cleaned_text = self.clean_text(content)
        words = self.extract_words(cleaned_text)
        
        for word in words:
            word_data = self.word_data[word]
            
            # Update frequency and files
            word_data['frequency'] += 1
            word_data['files'].add(filepath)
            
            # Update first seen date if not set or if this file is older
            if (word_data['first_seen_date'] is None or 
                mod_time < word_data['first_seen_date']):
                word_data['first_seen_date'] = mod_time
            
            # Mark as new if first seen in the last month
            if word_data['first_seen_date'] >= self.cutoff_date:
                word_data['is_new'] = True

    def scan_directory(self, directory: str):
        """Recursively scan directory for markdown files."""
        print(f"Analyzing files modified since: {self.cutoff_date.strftime('%Y-%m-%d')}")
        
        total_files = 0
        new_files = 0
        
        for root, _, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.md'):
                    filepath = os.path.join(root, file)
                    mod_time = datetime.fromtimestamp(os.path.getmtime(filepath))
                    
                    total_files += 1
                    if mod_time >= self.cutoff_date:
                        new_files += 1
                        self.process_file(filepath)
        
        print(f"\nProcessed {new_files} new/modified files out of {total_files} total markdown files")

    def generate_report(self, output_file: str):
        """Generate CSV report with word frequencies and file paths."""
        # Convert data to format suitable for DataFrame
        rows = []
        for word, data in self.word_data.items():
            if data['is_new']:  # Only include new words
                rows.append({
                    'word': word,
                    'frequency': data['frequency'],
                    'first_seen_date': data['first_seen_date'].strftime('%Y-%m-%d'),
                    'file_paths': '|'.join(sorted(data['files']))
                })
        
        # Create DataFrame and sort by first seen date, then frequency
        df = pd.DataFrame(rows)
        if not df.empty:
            df = df.sort_values(['first_seen_date', 'frequency'], 
                              ascending=[False, False])
            
            # Save to CSV
            df.to_csv(output_file, index=False)
            print(f"\nReport generated successfully: {output_file}")
            
            # Print summary statistics
            print(f"\nNew vocabulary statistics:")
            print(f"Total new unique words: {len(df)}")
            print(f"\nTop 10 most frequent new words:")
            print(df.head(10)[['word', 'frequency', 'first_seen_date']].to_string())
            
            # Group by date analysis
            date_groups = df.groupby('first_seen_date').size()
            print(f"\nNew words by date:")
            print(date_groups.to_string())
        else:
            print("\nNo new words found in files modified within the last month.")

def main():
    # Get directory path from user
    directory = input("Enter the directory path to analyze: ")
    output_file = "new_vocabulary_analysis.csv"
    
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    analyzer = MarkdownVocabularyAnalyzer()
    print(f"Analyzing markdown files in {directory}...")
    analyzer.scan_directory(directory)
    analyzer.generate_report(output_file)

if __name__ == "__main__":
    main()