# Welcome to Integrating Deep Learning with Classification of Sickle Red Blood Cells (RBC)

## Introduction 
A key component of [sickle cell disease](https://en.wikipedia.org/wiki/Sickle_cell_disease) (SCD) morbidity is periodic recurrence of painful [vaso-occlusion](https://en.wikipedia.org/wiki/Vaso-occlusive_crisis) and blood flow alteration, where sickle cell adhesion to the endothelial layer and the stiffness of red blood cell (RBC) membranes are the primary mechanisms. 



<p align="center">
<img src="https://user-images.githubusercontent.com/61917512/76152290-d2b4b400-608b-11ea-9e57-af36ea29d922.png" alt="pipeline img" height="80%" width="80%">
</p>

## Getting Started 

To help with debugging and understanding the model and pipeline, there is one main script 
([Main.ipynb]()) that calls all of the 
neccsesary functions to complete the pipeline. In addition, there is a corresponding Google Colab version
([Main2_google-collab.ipynb]()).  There is no need for user input in terms 
of deciding on specific parameter or model specifications. Below this text, we will present a walkthrough for the main script with visualizations. Here is the step 
by step walkthrough for the pipeline: 

### Main Script 

### Animation that Illustrates Phase I in the Pipeline
The top plot is the whole channel, consisting of stiched together mosaic images. The green box scanning across the channel corresponds 
to the two bottom plots, where the left and the right plot is the segmented and the binarized versions of the cropped image tile. Within 
the bottom two plots, the red pixels (right plot) and white pixels (left plot) corresponds to the segmented adhered cell mask and the 
binarized adhered cell mask. 

<p align="center">
<img src="https://user-images.githubusercontent.com/61917512/82155779-479f2980-9845-11ea-805e-e1160ebbc458.gif" 
height="100%" width="100%">
</p>


### Animation that Illustrates Phase II in the Pipeline
The top plot is the extracted object during `Phase 1` while the the bottom three plots corresponding to the output classes during `Phase 2`.

<p align="center">
<img src="https://user-images.githubusercontent.com/61917512/82156725-fdb94200-984a-11ea-9301-dc9e62e135ed.gif" 
height="100%" width="100%">
</p>

## Installation
    
To use DeepLearning-SCDBiochip functionality, please install within conda:

```
git clone https://github.com/InterxPim/Models.git

pip install -r requirements.txt
```

A quick and easy walkthrough to monitor adhered sRBC on large whole microchannels, functionalized with laminin can be illustrated here: [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Mohamed-Aziz-Mhadhbi/Drepanocytose/blob/main/Main_Drepanocytose.ipynb)


