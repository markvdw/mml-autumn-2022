# Mathematics for Machine Learning
Autumn 2022
Lecturers: [Mark van der Wilk](https://mvdw.uk), [Yingzhen Li](http://yingzhenli.net/home/en/)

Lecture materials for the Imperial College London course "Mathematics for Machine Learning". Some material is based on an earlier version of the course by [Marc Deisenroth](https://www.deisenroth.cc/). Lecture recordings are available on [Panopto](https://imperial.cloud.panopto.eu/Panopto/Pages/Sessions/List.aspx?folderID=ae57ded4-ce3a-42a1-9968-aedd014a24aa).

## Contributing
We welcome any suggestions and fixes from students. For those who make contributions, there will be cake.

If you want to make a contribution, please fork the repo, and make a pull request.

## Syllabus
Below is a syllabus of the course, together with a rough plan for the term. This is subject to change.

- Pre-course exercises
    - Basic probability, events, mutual exclusivity, independence, RVs
    - Probability densities, multivariate ones, multivariate integrals
    - Simple maximum likelihood
    - Statistical terminology (estimator, statistic, ...)
- Lecture 1: A (Hopefully (Reasonably)) Familiar Collection of Maths (MvdW)
    - Introduction (MvdW)
        - What is this course about?
        - Who is it for?
    - Setting the scene for Probability
        - Understanding the world using probability, models (shaking desk)
        - Notation of vector probability density (vectors as grouping of variables)
        - Maximum Likelihood (Recap from P&S)
        - Linear Regression from loss func and as MaxLik
    - Multivariate differentiation
        - Differentiation, by scalars and vectors
    - Multivariate calculus (revision)
- Lecture 2: Differentiation & Autodiff (MvdW)
    - Differentiation of vectors, general array differentiation
    - Index notation for multivariate calculus
- Lecture 3: Automatic differentiation (MvdW)
    - Computational Graph
    - Forward-mode autodiff
    - Backward-mode autodiff
    - Computational complexity guarantees ([see this](https://timvieira.github.io/blog/post/2016/09/25/evaluating-fx-is-as-fast-as-fx/))
- Lecture 4: Gradient Descent (YL)
- Lecture 5: Gradient descent applications: Linear & Logistic Regression (YL)
- Lecture 6 & 7: Multivariate Probability (YL)
- Lecture 8 & 9: Validation & Cross-validation (MvdW)
    - Overfitting
    - Estimating on the training set: Danger, underestimates error!
    - Unbiased estimate (recap from P&S)
    - High-probability bounds on generalisation error
- Lecture 10 and 11: Bayesian inference (MvdWL)
    - Principle of Bayesian inference
    - Gaussian conditioning from completing the square
    - Gaussian conditioning from a big joint distribution
    - Bayesian Linear Regression
    - Exercises: Simple Bayesian inference (coins), derive BLR.
- Lecture 12: Bias-variance trade-off (YL)
- Lecture 13 & 14: Dimensionality Reduction & PCA (YL 2L)

## Building the LaTeX sources
If you are using MacOS or Linux and have docker [installed]
(https://docs.docker.com/get-docker/) you can build the exercises from source
using `./bin/compile_exercises.sh`. Similarly, you can build non-handout
versions of the slides (i.e. without animations) using
`./bin/compile_course_slides.sh`.Unfortunately we still don't have a native
Windows script, feel free to contribute one if you are a Windows user and you
will be rewarded with cake!
