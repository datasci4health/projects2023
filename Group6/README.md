<h2> Project:  Histopathology breast cancer image classification using supervised learning</h2>

<h2> Projeto: Classificação de imagens histopatológicas de câncer de mama usando aprendizado supervisionado</h2>



This project originated in the context of the activities of the postgraduate discipline Health Data Science and Visualization, offered in the first half of 2023, at Unicamp 


| Name | RA | Specialization |
| -------- | -------- | -------- |
| Natalia Gil Canto  | 232881  | Electrical and Computing Engineering  |
| Sadeeq Olalekan Bello  | 198346  | Computing - Leader Github - Lekzyboi |
| Temitope Kola Adebowale | 256247 | Computing  |
| Suelen Aparecida Ribeiro de Souza  | 252483 | FCM |


# Summary Description of the Project

Breast cancer is a significant health issue affecting millions of women worldwide, and early detection is critical for improved patient outcomes. Histopathology analysis is a fundamental tool used to identify cancerous tissue, and it is a manual task performed by trained histopathologists. Based on that, in this project we aim to explore the use of supervised learning techniques to classify breast cancer histopathology images. Specifically, we will investigate whether a machine learning technique can be able to identify specific features or patterns in histopathology images that are indicative of breast cancer.
The importance of this project lies in the critical role of histopathology analysis in cancer detection. The current manual process is time-consuming and labor-intensive, and there is a significant potential for human error. We believe that by developing a classification model that accurately reproduces the manual task of histopathology analysis, we are making a meaningful contribution to the fight against breast cancer. 
Also, the results of the model classification of the histopathology images will be analyzed by a biomedical scientist with experience in histology. This analysis will validate the model’s performance and identify any areas for improvement. Therefore, by combining the expertise of the biomedical scientist with the power of a supervised learning technique, we aim to develop an accurate and reliable breast cancer diagnosis tool.

Link to video  [Link](https://youtu.be/T3a6fJ4nMLk)


# Research Questions
* Research question: Can supervised learning be used to identify specific features or patterns in histopathology images that are indicative of breast cancer? 


# Databases and Evolution

##  Database Studied but not Adopted
| Database | Web Address| Descriptive Summary |
| -------- | -------- | -------- |
| Human Against Machine (HAM10000) | [Link](https://www.kaggle.com/datasets/surajghuwalewala/ham1000-segmentation-and-classification?datasetId=1370616)  |  A large collection of multi-source dermatoscopic images of common pigmented skin lesions|

This dataset consists of 10,000 sample images with six different classes of skin lesions, they are Actinic keratoses and intraepithelial carcinoma / Bowen's disease (AKIEC), basal cell carcinoma (BCC), benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, BKL), dermatofibroma (DF), melanoma (MEL), melanocytic nevi (NV), vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and haemorrhage, VASC). 


All the datasets can be accessed through two main files. The first is composed of the images in .jpg format and the second is a .csv file that contains the image's names and the classes per image. Some examples of the structure of the data can be seen in the image below.

![Dataset Description](./assets/Dataset_NA.png)


During the exploratory data analysis, it was discovered that the classes are imbalanced, this was an interesting observation since the first idea of the project was to explore different data augmentation techniques on the health image dataset. However, the initial proposal was adapted to a scenario where we can have an insightful contribution from the health specialist in the team, and also,  based on the analysis of the problem itself, we concluded that in a daily routine, it wouldn't be a very useful tool for a doctor to work with. Therefore, this dataset was discarded.

##  Database Studied and Adopted

| Database | Web Address| Descriptive Summary |
| -------- | -------- | -------- |
| Breast Histopathology Images | [Link](https://www.kaggle.com/datasets/paultimothymooney/breast-histopathology-images)  |  Invasive Ductal Carcinoma (IDC) tissue regions in slide images (WSI) of breast cancer |

* The original dataset consists of 162 whole-mount slide images of Breast Cancer (BCa) specimens scanned at 40x. From that, 277,524 patches of size 50 x 50 were extracted (198,738 IDC negative and 78,786 IDC positive). 
* Each patch’s file name is of the format: u_xX_yY_classC.png: e.g., 10253_idx5_x1351_y1101_class0.png. 
* Where u is the patient ID (10253_idx5), X is the x-coordinate of where this patch was cropped from, Y is the y-coordinate of where this patch was cropped from, and C indicates the class where 0 is non-IDC and 1 is IDC. From the patient ID, we could observe that 279 patients are present on the dataset. Below we can see some examples from each class.

### Class 1

![Class 1 Patches](./assets/Class-1.png)

### Class 0

![Class 0 Patches](./assets/Class-0.png)



                                                                                    
To understand these images, we can proceed with a more detailed analysis of the problem and its main characteristics:

When breast cancer is detected early on, there is approximately a 95% chance of a cure. Histopathological images are considered the gold standard for diagnosing breast cancer; however, the histological technique and analysis are artisanal processes, and the interpretation of these images is time-consuming and can vary from one professional to another, depending on their experience (Brancati et al., 2022). There is also the risk of misdiagnosis, which can have serious consequences for the patient. Currently, there is a high demand for histological analysis that outweighs the number of skilled pathologists available. 


To be able to analyze and identify abnormal regions affected by the tumour, it is necessary to have a good understanding of the morphology, i.e., the shape of healthy cells and the normal composition of the organ being analyzed. 


In recent years, deep learning has gained prominence in this field for pattern recognition and efficient execution of various tasks (Cruz-Rhoa et al., 2014). The shape of cells follows a pattern according to the organ and function they possess. As cells deviate from this pattern and continue to multiply, they accumulate mutations and become increasingly different from the healthy cells from which they originated. The accumulation of mutations is classified as neoplasia, and the more these different cells multiply, the more aggressive the tumour becomes. Invasive ductal adenocarcinoma accounts for almost 80% of all breast cancer cases.


The tumour formed by clusters of neoplastic cells stimulates fibroblasts, which in turn stimulate the production of collagen fibres, leading to a desmoplastic reaction, visually identified by groups of cells arranged in rows. The clustering of mutated cells presents a cribriform appearance and visually resembles a sieve. The peripheral regions containing clustered white circular structures are adipose tissue cells, commonly known as fat-storing cells. Invasive ductal adenocarcinoma tends to expand into adipose tissue, and this event is related to the malignancy of the tumour (Aquino et. al., 2017). Cellular masses can also be observed in blood vessels and lymphatics, known as emboli. This event indicates that the tumour is seeking to invade regions beyond the breast, also known as metastasis. Veins can be identified by a ring lined with a thin layer of muscle cells (thin and elongated cells). 


In normal tissue, lymph nodes are important nodules for filtering and removing harmful substances from that region. Visually, they are identified as clusters of immune system cells. 
It is also possible to identify, in certain images, the presence of mammary glands with a flower-like shape, surrounded by a layer of cells (Anatpat, 2023). 


In addition to the mentioned findings, it is possible to locate lymphocytes, which are immune system cells and have slightly larger nuclei than the cells present in the breast. Mitoses, the events in which a cell multiplies through cell division, are also present. In these cases, cells have a denser nucleus and, in some instances, an elongated shape (Anatpat, 2023). 

Based on this information, we could plot and get some insights about the data. First, we have a plot presenting the number of patches per patient, second, we have a plot that highlights the percentage of an image that is composed of cancer cells, then, we can see how many patches there are on the dataset per class, where 0 represents “no cancer” and 1 the class “cancer”.

![Exploratory Analysis of the Patches](./assets/Patches.png)


From the first plot, we can observe a high variation in the number of patches per patient, with a mean of around 1000. This observation makes us think that, if the patches are the same size (50x50) per patient and the total number is still different, maybe the full images per patient have different sizes or some data is missing. However, at the moment, we believe that this is not a problem since the classification models are going to work with the patches as input, but, we do agree that we need to be careful about preserving data from the same patient in the same set (e.g., train, validation and test sets).

From the second plot, we can also see variations between the percentage of cancer cells on the images, with a mean of around 20%, this is important for us because from that we can assume that most of the images from the dataset contain more healthy cells than cancer cells, which correlates to the last plot that will be discussed in the sequence. 

From the third plot, we can get how much data from classes 0 or 1 are present on the dataset, and, based on that, we can clearly see we have an imbalance between them, which requires the decision of how we are going to deal with this type of scenario since this could cause problems on the learning process of the classification models. To deal with that, we have some options: apply data augmentation techniques to increase the samples from class 1; truncate the samples from class 0; or, make some adjustments on both at the same time. The implications related to each option will be evaluated later.

Also, the figure below shows some examples from the dataset for 6 different patients. Each image is composed of patches from that patient that are related to class 0 (pink circles) and 1 (blue circles). From that, we can confirm some of the insights we had from the plots above, that are: just a small percentage of the images contains cancer cells, and most of them are healthy cell, which justifies the classes being imbalanced; also, we can clearly see differences on the number of patches per patients since the x-y axis have different total numbers and the circles from the plots may appear in different distances from each other, which highlights that some patients may have images with different sizes or that are some missing patches per patient.

![Patient Patches](./assets/patient.png)




# Methodology


We are going to explore machine learning techniques, especially a supervised learning technique to classify breast cancer histopathology images. We aim to explore the results of the classification considering multiple metrics, such as: precision, recall, accuracy, false positive rate, false negative rate, and so on. Also, the metrics results and the mistakes made by the model are going to be evaluated by a biomedical scientist with experience in histology, so we can understand and adjust the hyperparameters of the model accordingly to produce a reliable and accurate model.


# Tools

Python, Google Collab, Deep Learning Libraries ( Scikit-learn, Tensorflow) , Data visualization libraries ( Matplotlib, seaborn, plotly ) and whatever tools needed to complete the project.

# Schedule

| Date | Task | Expected Delivery |
| -------- | -------- | -------- |
| May 10 | Data Exploration | May 15|
| May 15 | Baseline Model (EfficientNet, ResNet, DensNet) | May 31|
| June 1 | Hyperparameter tuning and model improvement | June 7 |  
| June 7 | Final Report | June 12 |
| June 13 | Presentation | June 18 |

## References
References:

* Aquino, R. G. F. D., Vasques, P. H. D., Cavalcante, D. I. M., Oliveira, A. L. D. S., Oliveira, B. M. K. D., & Pinheiro, L. G. P. (2017). Invasive ductal carcinoma: the relationship between pathological characteristics and the presence of axillary metastasis in 220 cases. Rev. Col. Bras. Cir., 44(2), 163–170. doi:10.1590/0100-69912017002010.

* Brancati N, Anniciello AM, Pati P, Riccio D, Scognamiglio G, Jaume G, De Pietro G, Di Bonito M, Foncubierta A, Botti G, Gabrani M, Feroce F, Frucci M. BRACS: A Dataset for BReAst Carcinoma Subtyping in H&E Histology Images. Database (Oxford). 2022 Oct 17;2022:baac093. doi: 10.1093/database/baac093. PMID: 36251776; PMCID: PMC9575967.

* Cruz-Roa, A., Basavanhally, A., González, F., Gilmore, H., Feldman, M., Ganesan, S., … Madabhushi, A. (2014). Automatic detection of invasive ductal carcinoma in whole slide images with convolutional neural networks. Medical Imaging 2014: Digital Pathology. doi:10.1117/12.2043872 

* UNICAMP. Department of Pathology Anatomy (Anatpat). Accessed on May 16, 2023. Available at: anatpat.unicamp.br.





