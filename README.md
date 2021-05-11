# Neurus

<h3>Used packages📦</h3>

* torch
* pandas
* matplotlib.pyplot

and jupyter notebook (https://jupyter.org/)

<h3>Getting started.🏋️</h3> 

To build env, use
```bash
$ conda env create -f pytorch_env.yml
```

To activate this environment, use
```bash
$ conda activate pytorchenv
```

To activate this environment, use
```bash
$ conda deactivate
```

To open Jupyter Notebook, use
```bash
$ jupyter notebook
```

<h3>What has been done?🤖</h3>
  
Three neural networks were created with a different approach to processing the dataset. <br>
Initially, I had difficulties with processing the original dataset, usually I gave the formation of the dataset to a class called **ImageFolder** from the **torchvision.datasets** package and did not have an understanding of working with custom datasets.  <br>
Temporarily I made it easy for myself by creating a **data_sorder.py** script, it split the source data for me into a convenient form. 
However, later, having figured out how this should be done, I prepared a dataset class to work with this form of data presentation. <br>
There were two approaches to training the neural network - manual description of parameters and transfer lerning from the **densenet121**
<br>
Dataset must be placed in 
```bash
$ path_to_project/Data
```

Enjoy!🌺
