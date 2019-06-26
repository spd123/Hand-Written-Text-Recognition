

Handwritten Text Recognition (HTR) system implemented with TensorFlow (TF) and trained on the IAM off-line HTR dataset.
This Neural Network (NN) model recognizes the text contained in the images of segmented words.
As these word-images are smaller than images of complete text-lines, the NN can be kept small and training on the CPU is feasible.
3/4 of the words from the validation-set are correctly recognized and the character error rate is around 10%.



## Run demo

go to the `src/` directory and run `python web.py`.
Upload the input image and the expected output is received.

> python main.py
Validation character error rate of saved model: 10.624916%
Init with stored values from ../model/snapshot-38
Recognized: "  "
Probability: 0.96625507


Tested with:

* Python 2 and Python 3
* TF 1.3, 1.10 and 1.12
* Ubuntu 16.04



The data-loader expects the IAM dataset  (or any other dataset that is compatible with it) in the `data/` directory.
Follow these instructions to get the dataset:

1. Register for free at this [website](http://www.fki.inf.unibe.ch/databases/iam-handwriting-database).
2. Download `words/words.tgz`.
3. Put the content (directories `a01`, `a02`, ...) of `words.tgz` into `data/`.


If you want to train the model from scratch, delete the files contained in the `model/` directory.
Otherwise, the parameters are loaded from the last model-snapshot before training begins.
Then, go to the `src/` directory and execute `python main.py --train`.
After each epoch of training, validation is done on a validation set (the dataset is split into 95% of the samples used for training and 5% for validation as defined in the class `DataLoader`).
If you only want to do validation given a trained NN, execute `python main.py --validate`.

