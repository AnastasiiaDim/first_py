def skills_list(skills):
    return len(set(skills)) # len returns amount, set removes duplicates

skills_list(["python", "java", "python", "sql", "json", "python"])

