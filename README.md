# Requirements

- Tensorflow
- Keras
- Graphviz [https://www.graphviz.org/]
```python
conda install graphviz
# Or install manually (Check https://www.graphviz.org/)
```


# Pokemon-AutoEncoder
VAE base Pokemon-AutoEncoder Project

VAE를 활용한 포켓몬데이터에 대한 VAE를 통한 Generating 프로젝트입니다.

전처리와 VAE모델 파일로 구성되어 있습니다. 

# Preprocessing
## Origianl data set
<img src="./pokemon-dataset/Overview/Original.PNG" width="600">

※    In Images folder 120x120 Pokemon Image files [809pokemons data]

## Images Resized and Regular image formated(PNG) data set
<img src="./pokemon-dataset/Overview/Resized.PNG" width="600">
※    In Preprocessed folder 56x56 Pokemon Image files [809pokemons data]

## Images npy matrix(.npy) data set
<img src="./pokemon-dataset/Overview/Matrix.PNG" width="600">
※    In MatrixPreprocessed folder 56x56 Pokemon Image files [809pokemons data]




# Model
## VAE Model Overview
Adapt VAE Model

<img src="./Images/Example1.png" width="600">

- Simple Structure

<img src="./Images/Example2.jpg" width="400">

- Simple Structure


## VAE Model Result
<img src="./Pokemon_VAE/Figure_1.png" width="400">  <img src="./Pokemon_VAE/Figure_2.png" width="400">
<img src="./Pokemon_VAE/Figure_3.png" width="400">  <img src="./Pokemon_VAE/Figure_4.png" width="400">


