# Feature extraction in medical image for classify Patients with Tourettes Syndrome

## Purpose
This repository contains the trained models and scripts used for our paper titled "Detecting Tourette’s Syndrome in Anatomical Regions of the Brain through MRI Analysis and Naive Bayes Classifier" and "Adding Dimensionality Reduction analysis of Texture descriptors for Tourette’s Syndrome classification". Our work focuses on utilizing texture feature to classify Tourette's Syndrome using classfication via machine learning (ML).

## Directory Structure
- `models/`
  - Contains the Generate descriptor Matrix, descriptor and classify models for two different architectures: Support Vector Machine(SVM) and Navie Bayes(NB).
  - Each architecture has two different dataset: `TS group` and 'Normal Control group'
  - The models are emplemented in scikit-learn library.

## Descriptors
The descriptors provided in this repository are named as follows:
- Grey Level Co-ocurrence Matrix (GLCM)
- Gray Level Run Length Matrix (GLRLM)
- Gray Level Size Zone Matrix (GLSZM)
- Neighbouring Gray Tone Difference Matrix (NGDTM)

## Usage
To use these models for feature extraction or classify, please follow the instructions below.

The algorithm Binary_Matrix_and_start_descriptor.py is employed to generate a binary matrix from a brain segmentation DICOM or NIfTI file. This process results in a binary matrix representing individual brain regions, which can be used for feature extraction in subsequent steps.

Following this, the Generate_Descriptor_Matrix.py script is applied to the binary matrices produced by the previous step. This script performs texture feature extraction from the binary matrices, creating a descriptor matrix that captures the relevant texture characteristics of each brain region.

Once the texture feature matrix is generated, classification can be performed using either the Naive_Bayes_Classifier.py or SVM_Classifier.py. These classifiers apply machine learning techniques to categorize brain regions based on the extracted texture features.

Finally, the Graph_results.py script is used for graph-based analysis of the classification results, enabling the visualization and interpretation of the outcomes in a structured manner.



### Loading Models

## Running the Script
Ensure you have Sklearn installed: pip install scikit-learn
SVM: pip install svm
NB: pip install naive-bayes

Run the script: python load_model.py

## License

This repository is licensed under the MIT License.

## Citation

The citation will be updated once this paper is published. Our citation template is [1] for Naive Bayes classify and [2] SVM classify:

```vbnet
[1] @inproceedings{de2022detecting,
  title={Detecting Tourette's Syndrome in Anatomical Regions of the Brain through MRI Analysis and Naive Bayes Classifier.},
  author={De Barros, Murilo Costa and Duarte, Kau{\^e} Tartarotti Nepomuceno and Lee, Wang-Tso and Hsu, Chia-Jui and De Carvalho, Marco Antonio Garcia},
  year={2022}
}

[2] @article{de2024adding,
  title={Adding Dimensionality Reduction analysis of Texture descriptors for Tourette’s Syndrome classification},
  author={de Barros, Murilo Costa and Duarte, Kau{\^e} Tartarotti Nepomuceno and Lee, Wang-Tso and Hsu, Chia-Jui and de Carvalho, Marco Antonio Garcia},
  journal={SN Computer Science},
  volume={5},
  number={6},
  pages={775},
  year={2024},
  publisher={Springer}
}
```
