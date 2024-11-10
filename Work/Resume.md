---
URL: https://www.overleaf.com/project/662216c1aaa7879b26c4e7af
---
1. Recommendation system for user use Earable band
2. [[Secure Offline RAG System]]
3. [[Plasmid]]
# Advice

3. **Talk about people.** My Google manager always reminded me that he offered me a role ==because of my experience working with product managers and UX designers. Mention your experience working with cross-functional teammates.==
4. **Talk about impact.** The impact is why that bullet matters. If you can clearly explain why the impact of your work matters, then it shows you can see the bigger picture that everything you do is for the end user.
5. Định lượng
6. **Experience > Completion.** It's 100% okay to put unfinished projects or work on your resume. It's more important that the candidate know the material and not whether it was actually done. Leading a project half way **STILL COUNTS** as leading a project.

- You have ==previous experience in a fast-paced startup environment==
- You have ==excellent written and verbal communication skills==

Center for Biomedical Informatics, Vingroup Big Data Institute
### Earable

Research machine learning algorithms in the fields of:  
- Recommendation system, intelligent suggestion system.  
- Reinforcement learning, active learning, multi-armed bandit system.  
- Brain signal processing, brain-computer interfaces.

### Healthcare monitoring system using brainwave control

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