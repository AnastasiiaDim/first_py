def skills_list(skills):
    unique_count = len(set(skills)) # len returns amount, set removes duplicates
    print(unique_count)

skills_list(["python", "java", "python", "sql", "json", "python"])

