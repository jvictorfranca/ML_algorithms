import pandas as pd

from Classes.LinearRegressionTrainer import LinearRegressionTrainer

sheet = pd.read_excel("Supervised\LinearRegressionSimple\sheet.xlsx")

trainer = LinearRegressionTrainer(sheet)

trainer.fit("X", "Y")
print(trainer.alpha, trainer.beta)
print(trainer.get_r_squared())
print(trainer.predict_y(5))
print(trainer.predict_y_list([1, 3, 4]))