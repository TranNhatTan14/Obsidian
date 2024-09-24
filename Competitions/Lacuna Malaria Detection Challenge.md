# Description

Join us on Thursday, 26 September at 5pm GMT for a webinar. Sign up here --> [](https://lu.ma/mc6mqojy)[https://lu.ma/mc6mqojy](https://lu.ma/mc6mqojy)

Malaria is one of the world’s most fatal infectious diseases, responsible for hundreds of thousands of deaths annually. It is a [major public health issue in Africa](https://www.who.int/news-room/fact-sheets/detail/malaria), where it predominantly affects children under five and pregnant women. Quick and accurate diagnosis is essential for treatment and management of malaria, but traditional methods of diagnosis, such as microscopic examination of blood slides, are resource-intensive and require skilled technicians, which are often scarce in rural and remote areas.

The objective of this challenge is to develop a multiclass object detection and classification model that can accurately identify and classify malaria parasites in blood slide images, specifically addressing diagnostic needs in Africa. Participants are required to create a machine learning model that can detect the [trophozoite stage of malaria](https://www.cdc.gov/malaria/php/surveillance/appendix-a-malaria-lifecycle.html), and differentiate between infected and uninfected blood cells.

A scalable machine learning solution could be implemented in large-scale screening and early warning programs to detect and control malaria outbreaks. Automated diagnostics can also alleviate the burden on healthcare workers, allowing them to focus on treatment and patient care, and improving the efficiency of healthcare systems in resource-limited settings.

Learn more about malaria [here](https://www.medmastery.com/guides/malaria-clinical-guide/how-identify-type-malaria-blood-smear). 

About Lacuna Fund ([lacunafund.org](https://lacunafund.org/))

Can you categorise parasites and blood cells in microscopic images from malaria patients?

# Evaluation

The error metric for this competition is [Mean Average Precision @ Intersection over Union(IoU) threshold -0.5](https://kharshit.github.io/blog/2019/09/20/evaluation-metrics-for-object-detection-and-segmentation).

Your submission file should look like this:

Image id     class             confidence  ymin  xmin  ymax  xmax

ID_2TZLLT80  WBC                   0.5     130   12    340   300

- Image_Id: is the Id assigned to each image. Note, that each image can have more the one object , which translates to more than one bounding box.
- Class: is the particular bounding box classification, i.e.,, trophozeite, White Blood Cell.
- Confidence score: each object detector model gives the confidence score of each bounding box predicted in an image; this value is used to sort the bounding boxes.
- (ymin, xmin, ymax, xmax)  The values of the bounding box as per the PASCAL implementation. The train data has(xmin, ymin, width, height), incase your model does produce the same structure, you need to convert it the required format.

Please note that we will not tell you if you are missing an image in your submission file. You will need to make sure you have submitted a prediction for each image.

Resource Restrictions

These models will likely need to be applied at scale, so large ensembles aren’t encouraged. To incentivise more lightweight solutions, we are adding an additional submission criteria: your submission should take a reasonable time to train and run inference. Specifically, we should be able to re-create your submission on a single-GPU machine (eg Nvidia A100) with less than 20 hours’ training and two hours’ inference.

# Data

About

The images in the dataset were captured by placing a smartphone over a microscope to capture the Field of View (FOV) of the blood slide through the eyepiece of the microscope. Along with the image, the slide from which the image was captured, the stage micrometer readings of the microscope, and the objective lens settings were recorded, and a maximum of 40 images was captured from each slide.

This blood slide image dataset was curated to facilitate using Computer Vision techniques for quick and accurate diagnosis of malaria in low-resource settings. This dataset adds to existing malaria microscopy datasets and can be used to improve machine learning models to generalise to data collected in other communities like Uganda.

There are 2 747 images in the train and 1 178 in the test.

Access the images here: [https://drive.google.com/file/d/16T40TdpaB8VXohm50SySREwrzbuPcJBC/view?usp=sharing](https://drive.google.com/file/d/16T40TdpaB8VXohm50SySREwrzbuPcJBC/view?usp=sharing)