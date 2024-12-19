# Detecting Tourette’s Syndrome in Anatomical Regions of the Brain through MRI Analysis and Naive Bayes Classifier

## Purpose
This repository contains the trained models and scripts used for our paper titled "Detecting Tourette’s Syndrome in Anatomical Regions of the Brain through MRI Analysis and Naive Bayes Classifier". Our work focuses on utilizing texture feature to classify Tourette's Syndrome using classfication via machine learning (ML).

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
To use these models for transfer learning or inference, please follow the instructions below.

### Loading Models

## Running the Script
Ensure you have Sklearn installed: pip install scikit-learn
SVM: pip install svm
NB: pip install naive-bayes

Run the script: python load_model.py

## License

This repository is licensed under the MIT License.

## Citation

The citation will be updated once this paper is published. Our citation template is:

```vbnet
@inproceedings{de2022detecting,
  title={Detecting Tourette's Syndrome in Anatomical Regions of the Brain through MRI Analysis and Naive Bayes Classifier.},
  author={De Barros, Murilo Costa and Duarte, Kau{\^e} Tartarotti Nepomuceno and Lee, Wang-Tso and Hsu, Chia-Jui and De Carvalho, Marco Antonio Garcia},
  year={2022}
}
```
