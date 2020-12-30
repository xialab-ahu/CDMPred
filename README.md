# CDMPred
CDMPred: a cancer driver missense mutation predictor for distiguishing driver mutations from passenger mutations.

Take Windows10 as an example, almost the same in Linux system. 

The prediction procedure is as follows:

1. create an enviroment using anaconda
> conda create -n cdmpred python=3.7

2. activate the enviroment
> conda activate cdmpred

3. pip install the requirements
> pip install -r requirement.txt

4. run the instruction as below
> python predict_final.py -i "./for_test.csv"

5. the prediction results will be printed.

For developers who want to run their own mutations data, just replace the "for_test.csv" with the corresponding encoded features by a dockerized tool,  the Cancer-Related Analysis of Variants Toolkit (CRAVAT, https://hub.docker.com/r/karchinlab/cravatmupit/) or the tool of SNVbox (https://karchinlab.org/apps/appSnvBox.html).
