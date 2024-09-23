---
links:
  - "[[Kaggle]]"
  - "[[Neuroscience]]"
  - "[[Competitions]]"
---
1. What is spectrograms
What is spectrogram in EEG?

The central tool in quantitative EEG, the “spectrogram,” also known as **color spectral array or color density spectral array**, is standard in most quantitative EEG software. The spectrogram is typically displayed as a three-way plot of time on the x axis, frequency on the y axis, and power as color.

A spectrogram is a visual way of **representing the signal strength, or “loudness”, of a signal over time at various frequencies present in a particular waveform**. Not only can one see whether there is more or less energy at, for example, 2 Hz vs 10 Hz, but one can also see how energy levels vary over time.

Spectrogram is of advantage to **express speech signal than other features in time-domain or frequency-domain alone**, combining the merit of both domains and showing the relationship of time, frequency, and amplitude directly.

In the datasets used in previous works, in the stage of the extraction of the fingerprint of each audio file, constant spectrogram parameters (**window length, overlap, FFT number**) are used in general while these files are recorded in the dataset.


1. How to produce Kaggle’s spectrograms
2. How to produce spectrograms from EEG waveform

[How to Install Without Internet](https://www.kaggle.com/c/severstal-steel-defect-detection/discussion/113195)

[Severstal: Steel Defect Detection](https://www.kaggle.com/c/severstal-steel-defect-detection/discussion/113195)

one example how to do it is to download and save the pip-wheel of torch geometric and create a dataset with it. Then in the submission kernel put this dataset as input and pip install from that wheel

[Gunes Evitan | Discussion Grandmaster](https://www.kaggle.com/gunesevitan/discussion)

[Dieter | Discussion Grandmaster](https://www.kaggle.com/christofhenkel/discussion)

[Data](https://www.notion.so/Data-b6ca64be067d498da77354c8ea38b4fc?pvs=21)

<aside> 💡 We can transfer from Kaggle to Google Colab

</aside>

[HMS - Harmful Brain Activity Classification](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification)

This leaderboard is calculated with approximately 35% of the test data. The final results will be based on the other 65%, so the final standings may be different.

### Note

- Spectrograms for CNN
- EEG with Transformer

### Background

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/471439](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/471439)

[**Video available. Introductory webinar on the competition**](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/472688)

[**Grad Cam - What is important in Spectrograms?**](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/472976)

[Hard samples are more important](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/477461)

[Bridging the Gap between Cross-Validation and Leaderboard Scores [CV 0.44 – LB 0.47]](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/477498)

[[0.34] LB Gatekeeping](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/478602)

[Converting non-competition EEG signals to 10-minute spectrograms](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/479001)

### Relevant competitions

**Sleep states, time series classification**

[Child Mind Institute - Detect Sleep States](https://www.kaggle.com/competitions/child-mind-institute-detect-sleep-states/overview)

### Notebooks

[3 Model Ensemble(LB 0.37)](https://www.kaggle.com/code/kitsuha/3-model-ensemble-lb-0-37)

[HMS[BLEND]All Torch PublicModel SimpleBlend[LB.32]](https://www.kaggle.com/code/hideyukizushi/hms-blend-all-torch-publicmodel-simpleblend-lb-32)

**WaveNet**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/468684](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/468684)

**1D ResNet**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/471666](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/471666)

**EfficientNetB0 PyTorch**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/472092](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/472092)

**MultiModal Approach Raw Signals + Spectrograms**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/476000](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/476000)

**EffNetB0**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/477135](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/477135)

**Graph Neural Networks**

[Graph Neural Network-based EEG Classification: A Survey](https://arxiv.org/html/2310.02152v2)

**WaveNet PyTorch**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/477610](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/477610)

**EEG Signals in PyTorch**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/478195](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/478195)

**Resnet1D_GRU EEG Only Pytorch**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/478474](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/478474)

### Tools

- **EEG signals data processing**
    
    **Nilearn** - [https://nilearn.github.io/stable/index.html](https://nilearn.github.io/stable/index.html)
    
    Nilearn enables approachable and versatile analyses of brain volumes. It provides statistical and machine-learning tools, with instructive documentation & open community.
    
    It supports general linear model (GLM) based analysis and leverages the scikit-learn Python toolbox for multivariate statistics with applications such as predictive modelling, classification, decoding, or connectivity analysis.
    
    **MNE-Python** - [https://mne.tools/stable/help/index.html](https://mne.tools/stable/help/index.html)
    
    Open-source Python package for exploring, visualizing, and analyzing human neurophysiological data: MEG, EEG, sEEG, ECoG, NIRS, and more.
    
    Thanks for sharing! i'm looking foward MNE instead of librosa
    

### Data

- [Dataset: The Temple University Hospital Seizure Detection Corpus](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/479244)

**Patients**

[https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/471783](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/471783)

**EEG**

- [EEG 10-20 system](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/466735)
    
- EEG Column Name Explanation
    
    According to: [https://neurofeedbackalliance.org/brain-regions-and-neurofeedback/](https://neurofeedbackalliance.org/brain-regions-and-neurofeedback/)
    
    FRONTAL LOBES:
    
    - Left Hemisphere: Working memory, concentration, executive planning, positive emotions
        - Fp1
        - F3
        - F7
    - Right Hemisphere: Episodic memory, social awareness
        - Fp2
        - F4
        - F8
    
    PARIETAL LOBES:
    
    - Left Hemisphere: Problem solving, maths, complex grammar, attention
        - P3
    - Right Hemisphere: Spatial awareness, geometry
        - P4
    
    TEMPORAL LOBES:
    
    - Left Hemisphere: Word recognition, reading, language, memory (train for dyslexia)
        - T3
        - T5
    - Right Hemisphere: Object recognition, music, social cues, facial recognition
        - T4
        - T6
    
    According to: [https://biologydictionary.net/occipital-lobe/](https://biologydictionary.net/occipital-lobe/)
    
    OCCIPITAL LOBES:
    
    - Left Hemisphere: right-hand field of vision
        - O1
    - Right Hemisphere: left-hand field of vision
        - O2
    
    According to: [https://www.biorxiv.org/content/10.1101/2023.02.06.527390v1.full.pdf](https://www.biorxiv.org/content/10.1101/2023.02.06.527390v1.full.pdf)
    
    MOTOR CORTEX:
    
    - Left Hemisphere: movement of right hand
        - C3
    - Right Hemisphere: movement of left hand
        - C4
    
    The article states that these might not be the best locations to estimate hand movement but oh well. Hopefully won't affect accuracy of models :)
    
    According to: [https://openi.nlm.nih.gov/detailedresult?img=PMC3146818_1471-2377-11-82-1&req=4](https://openi.nlm.nih.gov/detailedresult?img=PMC3146818_1471-2377-11-82-1&req=4)
    
    Z just means midline so:
    
    - Fz: frontal lobe midline
    - Cz: motor cortex midline
    - Pz: parietal lobe midline
    
    According to: [https://www.verywellhealth.com/electrocardiogram-ekg-ecg-1745304](https://www.verywellhealth.com/electrocardiogram-ekg-ecg-1745304)
    
    An EKG is used to analyze heart rate and heart rhythm
    
- [EEG to Spectrograms](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/469760)
    
- [EEG relates to a Spectrogram](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8901534/)
    
- [https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467129](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467129)
    

**Spectrogram**

- [Spectrogram Data Acquisition Rate](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/466759)
    
- [Create Spectrogram From EEG](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467877)
    
- [Faulty spectrogram and EEG data](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467909)
    
- [How spectrograms for this competions were created?](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/468248)
    
- [Spec: LL + LP + RP + RR + Others](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/472444)
    
- [Do spectrograms contain more "information" than signals?](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/478391)
    
- Spectrograms with more than one EEG ID
    
    In train.csv, there are 2380 spectrogram ids that have more than one eeg id associated with them.
    
    What does that mean?
    
    I thought each spectrogram is a 10 minute window over a single eeg centered at the same time.
    
    There are 1950 unique patients. Each patient can have hours of readings. Kaggle split the EEG into 17089 files and the spectrograms into 11138 files. Alternatively, we could have had just 1950 EEG files and 1950 spectrogram files but they would have been too large files.
    

### Features

- Feature engineering
    
    - In the medical field, interpretability of the solution is key to understand what the model is doing
        
    - Hand-made interpretable feature engineering on raw EEG epochs with a classification machine learning model
        
        - Statistics on raw epochs of EEG signal (tme features)
        - Frequency features
        - Time-frequency features based on coefficients of the wavelet transform
        - Hjorth parameters: [Wikipedia link](https://en.wikipedia.org/wiki/Hjorth_parameters)
            
            The Hjorth parameters look really useful. The PDs and RDAs require a semi-constant frequency, so I imagine the Hjorth complexity would be useful here
            
        - Power Spectral density, Entropy features
        - Features from EEG waves: delta, theta, alpha, beta, gamma
            
    - Deep Learning approach as the deep model can learn informative features directly from the raw EEG signnals
    - CNN model for the best features learning approach
        

### Evaluating

- [CV vs LB Scores](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467915)
- [LB probing results in HMS-HBAC](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/471890)

### Discussion

- [How to get the correct subsets](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467110)
- [Merge targets](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467127)
- [Computing Vote Ratio's | Total Number Of Voters In Train Samples](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467163)
- [Time Window Labels Apply To | spectrogram_label_offset_seconds](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467292)
- [Physical Unit](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467655)

### Resources

- [Getting started with Brain Data (EEG)](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/466768)
- [EEG Basics](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467783)
- [Understanding terminologies with examples](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/467000)

[Understanding EEG: A Practical Guide for Patients and Families](https://www.youtube.com/watch?v=FpdyFMNEZRM)

**Research papers**

[EEG-Based Machine Learning: Theory and Applications](https://www.nzbri.org/resources/publications/657/Shoorangiz__2021.pdf)

[Multimodal Fusion](https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/discussion/469209)

**ACNS Critical Care EEG Terminology** (5 videos; much easier to digest than the link to the actual document):

[EEG Talk - ACNS Critical Care EEG Terminology 2021](https://www.youtube.com/playlist?list=PL1qAb9U_Ln6EO07t6SuqjZdgkwwRNOECr)

**Spectrograms** (3 videos; a pretty good intro to the theory and the interpretation of spectrograms in the context of this competition):

[EEG Talk - Spectrogram](https://www.youtube.com/playlist?list=PL1qAb9U_Ln6H3KH6B67SaLwecaBHEKgo_)