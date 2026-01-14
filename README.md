# Machine Learning

The focus of the project is model training, evaluation, and real-world prediction. Due to time constraints, the dataset will be selected from Kaggle. The most challenging part of building an AI system, which is data preparation, will be handled automatically. In the next step, the model will be trained, and each stage of the process, including evaluation and random seed selection, will be demonstrated. 

##### Objective
The objective of this project is to identify the best wine without tasting it. In order to achieve this, the dataset is divided into 13 features, listed below:
1. country
2. description
3. designation
4. points
5. price
6. province
7. region_1
8. region_2
9. taster_name
10. taster_twitter_handle
11. title
12. variety
13. winery

The project aims to build a predictive model that identifies wines through blind tasting, similar to how a master sommelier would. One key challenge is that sommeliers assign scores to wines based on their personal background. However, the features used to train the model are not directly linked to these subjective scores.

Instead, the model profiles sommeliers based on their past evaluations. These profiles can then be used by companies to predict which sommeliers are most suitable for evaluating specific types of wine.

`wine feature + someleir profile -> output.`

### Dataset Description
As mentioned before, the dataset is divided into 13 features following:
`['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'taster_name', 'taster_twitter_handle', 'title', 'variety', 'winery']`

There are 44 countires in the dataset, listed below:
1. Brazil
2. Romania
3. Argentina
4. US
5. Italy
6. Germany
7. Luxembourg
8. Macedonia
9. Bosnia and Herzegovina
10. Czech Republic
11. Egypt
12. Cyprus
13. Australia
14. Croatia
15. Israel
16. Ukraine
17. Moldova
18. India
19. Austria
20. South Africa
21. Switzerland
22. Georgia
23. Slovakia
24. Chile
25. Armenia
26. Hungary
27. Mexico
28. Portugal
29. Turkey
30. France
31. England
32. Peru
33. China
34. New Zealand
35. Lebanon
36. Canada
37. Serbia
38. Slovenia
39. Morocco
40. Bulgaria
41. Greece
42. Uruguay
43. Spain

Sample description: Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.

Additionally, there are 708 variety of wines and 129971 winery. 

##### Hierarchy of The Production
wein
└── country
    └── province
        └── region_1
            └── region_2




### TO-DO List

### Push To Repository
Please do NOT push directyl to the `main` branch. Create a new branch based on your
role, then opan a **pull request** on GitHub.

```bash
git add . # Stage all changes
git commit -m "Describe your changes." # Commits
git switch -c feature/modelling # Push the new branch to Git.
```
While adding commtit descriptions please use convertional commits.

```
feat: add relu activation function # add new feature to the project
fix: correct wrong logic # use for bug fixes/issues
docs: update README with conventional commits. # For documentation
build: add Dockerfile # everything related to build pipeline.
chore: update .gitignore # Update dependencies.
style: fix whitespaces # code changes but the logic does not.
refactor: simplify grade calculation loop # Make the code cleaner.
test: add tests # Add unit test and integration test etc.
perf: optimize grade calculation to reduce runtime # Optimizes the code.
revert: revert a commit. # Reverts a commit.
```