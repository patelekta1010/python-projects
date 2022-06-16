import pandas as pd

data = {
      'Students': ["bob", "ekta", "deep", "taksh"],
      'Maths': [67, 98, 87, 95],
      'Science': [96, 81, 97, 8],
      'E nglish': [45, 50, 78, 40]
}

students = pd.DataFrame(data, columns =["Students", "Maths", "Science", "English"])
print(students)