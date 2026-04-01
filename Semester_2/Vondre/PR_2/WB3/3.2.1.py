import pandas as pd

dt = pd.DataFrame({"оценка" : ["низкая","низкая", "средняя", "средняя", "высокая"]})
scale_mapper = {"низкая": 1, "средняя": 2, "высокая": 3}


dt["оценка"].replace(scale_mapper)
print(dt)