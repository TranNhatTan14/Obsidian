Require from big corp
Prepare pet project

# Natural Language Processing

### Chatbot

###### LLM

### Fraud detection if work in bank

###### Healthcare monitoring system using brainwave control

Research on emotion classification using EEG signals
1. Emotion classification using EEG signals
2. Health data: heart rate, calories, distance, steps, ...

Frenz Brainband: EEG, EOG, EMG

- Dữ liệu được xử lý như thế nào
- Time-frequency analysis
- segmenting the EEG signal into short overlaping time windows and applying FFT to each window
- Power Spectrail Density
- Spectral entropy
- Mean
- Variance
- STD

**Feature Extraction**
EEG signal is divided into a sequence of windows of length one second, with consecutive windows overlapping by 0.5 s
Features: mean, standard deviation, skewness, kurtosis, maximum, minimum, magnitude of the frequency component of each signal, obtained using a FFT

**Proposed and developed an emotion classification algorithm based on brainwave signals**
- Phân loại cảm xúc thành những nhóm nào
- Làm sao để phân loại cảm xúc từ tín hiệu sóng não
- Thuật toán sử dụng là RNN (GRU và LSTM)

**Datasets**

[EEG Brainwave Dataset: Feeling Emotions](https://www.kaggle.com/datasets/birdy654/eeg-brainwave-dataset-feeling-emotions)

**Electroencephalography (EEG) and Brain-Computer Interface (BCI):**

What were the main challenges in emotion classification using EEG signals, and how did you overcome them?
	- One of the main challenges in classifying emotions using EEG signals is the inherent noise and variability in the EEG data. To address this, I implemented signal processing techniques to clean the data and then applied machine learning algorithms to classify emotions. The feature extraction process was critical; I focused on frequency bands known to correlate with emotional states and used statistical features from these bands to train the classifiers.
	- Một vấn đê quan trọng là xử lý nhiễu
	- Thuật toán xử lý tín hiệu 
	- Applied thuật toán ML để có thể phân loại cảm xúc ở đây em thử dùng GRU và LSTM  
Can you discuss your approach to analyzing EEG/EMG/EOG signals and predicting user states such as focus and sleep stages?
    - My approach involved several stages: first, preprocessing the signals to remove noise and artifacts. 
    - Nhiễu là những gì?
    - Khử nhiễu như thế nào?
    - For sleep stage classification, I used time-frequency analysis to extract features that correlate with different sleep stages. 
    - N1
    - N2
    - Nhiệt độ cơ thể và nhịp tim giảm
    - N3
    - REM
    - Mắt chuyển động nhanh
    - To predict user states like focus or stress, I analyzed the power spectral density of different EEG frequency bands, as alterations in these bands are indicative of changes in focus and stress levels.
    - Điều khiển thông minh dựa trên chuyển động của mắt, khi ở trạng thái thư giãn thì xe sẽ đi thẳng, khi nhìn sang trái hoăc sang phải thì xe sẽ đi theo hướng
    - Làm sao để xác định xung (dưa trên tín hiệu như thế nào)
###### [Masked Face Detection with Illumination Awarenes](https://eprints.uet.vnu.edu.vn/eprints/id/eprint/4775/1/2022_ISMICT_arxiv%20version.pdf)

1. Real world dataset
2. [Low-Illumination Image Enhancement (LIIE)](https://sci-hub.se/downloads/2021-05-28/243e/wang2020.pdf)
3. SSD MobileNetV2 FPNLite
4. Jetson Nano

###### [Emotion classification of individuals in image based on facial expression and context](https://ujm.hal.science/ujm-04194014v1/document)

1. Most recent research: person detection, sequentially, real world application
2. EMOTIC and CAER-S datasets: public, context, random data transformation
3. Bottom-up Emotions Network: DETECT all the subjects and PRODUCE E discrete emotion maps directly from the raw image to ESTIMATE their emotion
4. Shared High-Resolution Network-W32 backbone with Spatial and Channel Attention Modules: emphasize discriminate regions and adaptive select more important channel of feature maps
5. Face detection: facial landmark

# Machine Learning
# Computer Vision

###### Image Processing
###### Detection
###### Face detection
- Haar feature
- Intergral image
- Computing Integral Image using Raster Scanning
- Mask face detecion
- Emotion detection

###### Recognition
- The more difficult problem of category or class recognition was also initiallly
- General object recognition falls into two broad categories: instance recognition and class recognition
- Extracting infomative 2D features
- Feature-based approaches
- bag of words, bag of features, bag of keypoint
- compute the distribution (histogram) of visual words found in the query image and compares this distrubution to those found in the training images
- Old
- SIFT, k-means, naive Bayesian, SVM, boosting

###### Context and scene understanding

- Context play a very important role in human object recognition
- Providing usefull semantic clues for general scene understanding

###### Face recognition

- Human-Computer Interaction
- Face recognizers work best when they are given images of face under a wide variety of pose, illumination, and expression (PIE) conditions
- Research have also studied the automatic recognition of facial expressions
- Face detection techniques can be classified as feature-based, template-based, or appearance-based

###### Classification

- Emotion classification

### Natural Language Processing

### Brain–Computer Interface

###### Electroencephalography

- How to collect EEG signal?
- Linear Algebra
- The introduction of numbers as coordinates is an act of violence
- Vector
- Physics 
- Computer Science
- Mathematic
- Một cái giống như Linear Algebra là gì
- Add
- Multiply
- Scaling
- The basis vector of the coordinate system
- What if we choose the different basis vector
- Linear combination
- The span of v and w is the set of all their linear combinations
- Linearly independent 
- The basis of a vector space is a set of linearly independent vectors that span the full space

---
### Programming

Delve into advanced concept such as OOP and Algorithm optimization.

Understanding how to write efficient, scalable code is crucial since AI applications often process large amounts of data. 

Practice by contributing to open-source projects or tackling complex problems that challenge your coding skills.

- Writing clean, efficient, and scalable code.
- Understand the principles of software engineering, including version control, testing, and debugging. 

### Data

Data is the lifeblood of AI. You must be adept at data preprocessing, which includes cleaning and normalizing data to ensure that your AI models are trained on high-quality datasets. 

###### Data Preprocessing

Cleaning and normalizing data to ensure AI models are trained on high-quality datasets

###### Data Manipulation Tools

Acquire skills in using tools that facilitate efficient data manipulation.

###### Database Management Systems

 Understand the workings and management of database systems to support robust AI solutions.

Learning to use data manipulation tools and understanding database management systems are also valuable skills. 

By mastering data handling, you'll ensure that your AI solutions are built on solid ground, leading to more accurate outcomes.

Learn to use tools like SQL, pandas, and Hadoop for efficient data manipulation and analysis.

Gain experience in handling big data, including knowledge of distributed computing frameworks such as Apache Spark, to manage and process large datasets effectively.

### [[Machine Learning]] and applications in real-world

 Stay abreast of emerging ML trends and frameworks, and practice by building and refining your own models.


[Cloud Computing Services - Amazon Web Services (AWS)](https://aws.amazon.com)

### Technology

Polar instead of Pandas

- Time management
- Enery management
- Priority

### Transfer Learning

### Knowledge

Information Technology

- Data Management
- System Design
- Data Structure & Algorithms
- Graph Theory
- Distributed Data Processing knowledge, Big Data processing (Hadoop, Spark)
- ETL flow building skills
- API
- Operating systems
- Slurm?
- Git and Git Flow
- Docker and Kubernete
- [Kubeflow](https://www.kubeflow.org/) and MLFlow
- Cloud and Edge device
- Exploratory Data Analysis (EDA)
- SQL
- Skills
    - Knowledge Distiller
    - Model Prune
    - Model Quantization

### Soft skills

- Teamwork
- Independent work

Reinforcement Learning

Computer Vision

- Image Processing
- Segmentation
- Object detection and recognition
- Image quality enhancement
- Image registration

AI Ethics

AI in Healthcare

AI in Finance

### **Reseach**

**Programming**

- **Python**
- C
- C++

### Deploy

- [ ] Edge devices, PC, Cloud
- [ ] Chuyển đổi mô hình dùng SNPE, TensorRT, TensorCore, ONNX


- **Top-down approach:** Learn code first, theory later.
- **Focus on NLP (Natural Language Processing):** If you're interested in other areas like computer vision, ask the author for recommendations.
- **Use Twitter:** Follow AI experts and engage in the community.

**1. Mathematics:**

- Linear algebra, calculus, probability, and statistics are fundamental for AI algorithms.
- [https://youtu.be/uZeDTwWcnuY?si=NOh8uFRfMTyUcopN](https://youtu.be/uZeDTwWcnuY?si=NOh8uFRfMTyUcopN)

**2. Tools:**

- **Python, Polar, C++, CUDA**
- **PyTorch**

**3. Machine Learning:**

- **Write algorithms from scratch.**
    - [Machine Learning From Scratch](https://github.com/eriklindernoren/ML-From-Scratch)

DSA

Machine Learning