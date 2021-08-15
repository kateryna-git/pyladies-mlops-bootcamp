# Feedback

Hereby my feedback for your repository. Congratulations on having participated in the bootcamp and on your efforts to 
complete it. You have good knowledge of Python programming, especially of directory structures.

## General

- Why is there no _requirements.txt_ or Conda environment file in the root directory?

- It is usually best to not save data in a code repository. If you are aware of this and
have it here due to limitations on storage, then please disregard this comment. Otherwise, you
could consider a storage solution from Azure.

- In the _README.md_, add at least instructions for installation and usage.

## Specific Files

Hereby feedback on some Notebooks. The rest of the files are difficult to interpret.

### create_batch_pipeline.ipynb
  - Do all imports at the top.
  - There is a repeated _from azureml.core import Workspace_.
  - Why do you set _vm\_size='Standard\_DS2\_v2'_, but in the text
  describe _Standard\_DS11\_v2_?
  - The use of a list comprehension inside a for loop can be replace with:
      ```python
      mini_batch = [os.path.join(dirpath, file) for file in filenames for (dirpath, dirnames, filenames) in os.walk("capstone-batch-data")]
      ```
  - The cell with _np.mean(result)_ and the following cell, are they in the wrong order?
  - The step for _Traverse the folder hierarchy and find the results file_ does not seem optimal. 
  Could you find a better way that does not require traversing the directories? Is the path to the file not known 
  beforehand, or can you not set it explicitly?

### evaluate_model_15min.ipynb
  - Why cut _load\_actuals|_mw_ into 3 only?
  - In the diagram output from _baseline\_predict.plot()_, the legend shows two variables, yet only one is plotted?
  - There is few text in the rest of the file, which makes it difficult to interpret.

### evaluate_model_daily_1.ipynb
  - Is the code here similar to that in _evaluate\_model\_15min.ipynb_?
