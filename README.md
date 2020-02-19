# Welcome to my repository for the Medium article I wrote on APIs, Docker and basic Machine Learning models

Thanks for checking this out. First train your own model with the training.py file.
Then, go ahead and poke around in it with the testing.py function.

Finally, when you're ready, in your terminal run `docker build -t mltag:latest .`

When that finishes building, type in `docker run -it -d -P mltag:latest` then `docker ps` and take not of the port
that your docker is exposing, it should look like `0.0.0.0:32768->8080/tcp` under `PORTS`

Go ahead and run a curl on it or in the browser as

`0.0.0.0:32768/related/c++`

### or...

you can just run `. boot.sh` from the root directory to get a local server on `0.0.0.0:8080` or you can run 
the `docker-build.sh` and have it do it for you :)

## The App
When you get the model set up, it should give you nice things like ```{"original":"machine learning","similar":[{"tag":"classification"},{"tag":"svm"},{"tag":"training data"},{"tag":"naivebayes"},{"tag":"text classification"},{"tag":"supervised learning"},{"tag":"document classification"},{"tag":"multilabel classification"},{"tag":"neural network"},{"tag":"unsupervised learning"}]}```

