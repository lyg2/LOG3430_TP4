import os

badHash = "c1a4be04b972b6c17db242fc37752ad517c29402"
goodHash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
commandTest = "python manage.py test"

os.system(f"git bisect start {badHash} {goodHash}")
os.system(f"git bisect run {commandTest}")
os.system("git bisect reset")
