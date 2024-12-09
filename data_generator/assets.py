import random
import string
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId
import random
from datetime import datetime, timedelta
from pymongo import MongoClient
from bson.objectid import ObjectId

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def random_name():
    names = [
        'Ram', 'Shyam', 'Surya', 'Ronak', 'Aarav', 'Vivaan', 'Aditya', 'Vihaan', 'Arjun', 'Sai', 
        'Reyansh', 'Ayaan', 'Krishna', 'Ishaan', 'Shaurya', 'Atharv', 'Aarush', 'Dhruv', 'Kabir', 
        'Ritvik', 'Rudra', 'Anay', 'Aarav', 'Aryan', 'Arnav', 'Advait', 'Aayush', 'Anirudh', 'Arhaan', 
        'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 'Aayush', 'Advik', 'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 
        'Aayush', 'Advik', 'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 'Aayush', 'Advik', 'Ahaan', 'Aarav', 
        'Aarush', 'Aayansh', 'Aayush', 'Advik', 'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 'Aayush', 'Advik', 
        'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 'Aayush', 'Advik', 'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 
        'Aayush', 'Advik', 'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 'Aayush', 'Advik', 'Ahaan', 'Aarav', 
        'Aarush', 'Aayansh', 'Aayush', 'Advik', 'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 'Aayush', 'Advik', 
        'Ahaan', 'Aarav', 'Aarush', 'Aayansh', 'Aayush', 'Advik', 'Ahaan', 'Aarav', 'Aarush', 'Aayansh'
    ]
    return random.choice(names)

def random_email():
    return f"{random_string(5)}@{random_string(5)}.com"

def random_role():
    return random.choice(['Applicant', 'Recruiter'])

def random_objectid():
    numbers = list(range(1234000, 1234200))
    return random.choice(numbers)
        
def random_dept():
    departments = [
        'Support', 'Development', 'QA', 'Security', 'Infrastructure', 'DevOps', 'Data Science', 'Product Management',
        'UX/UI Design', 'Network Engineering', 'Cloud Engineering', 'AI Research', 'IT Operations', 'Database Administration',
        'Technical Writing', 'Customer Success', 'Sales Engineering', 'IT Support', 'Business Analysis', 'Project Management'
    ]
    return random.choice(departments)

def random_title():
    titles = [
        'Software Engineer', 'Data Scientist', 'Product Manager', 'UX Designer', 'Network Engineer',
        'Security Analyst', 'Web Developer', 'AI Engineer', 'DevOps Engineer', 'Cloud Architect'
    ]
    return random.choice(titles)

def random_company_name():
    names = [
        'Amazon', 'Apple', 'Facebook', 'Google', 'Netflix', 'Microsoft', 'IBM', 'Intel', 'Cisco', 'Oracle',
        'Salesforce', 'Adobe', 'Dell', 'HP', 'NVIDIA', 'Qualcomm', 'VMware', 'Uber', 'Airbnb', 'Spotify',
        'Twitter', 'Snap', 'Pinterest', 'LinkedIn', 'Square', 'Shopify', 'Slack', 'Dropbox', 'Zoom', 'Palantir',
        'Reddit', 'GitHub', 'Stripe', 'PayPal', 'Tesla', 'SpaceX', 'Alibaba', 'Tencent', 'Baidu', 'JD.com',
        'Samsung', 'LG', 'Sony', 'Huawei', 'Xiaomi', 'Lenovo', 'ASUS', 'Acer', 'Toshiba', 'Panasonic'
    ]
    return random.choice(names)

def random_company_id():
    numbers = list(range(34000, 34200))
    return random.choice(numbers)

def random_blog_id():
    numbers = list(range(456000,456200))
    return random.choice(numbers)

def randon_state():
    states = [
        'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida', 
        'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 
        'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 
        'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 
        'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 
        'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
    ]
    return random.choice(states)

def random_skills():
    skills = ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'React', 'Node.js', 'Django']
    return random.sample(skills, random.randint(1, 5))

def random_salary():
    min_salary = random.randint(30000, 50000)
    max_salary = min_salary + random.randint(10000, 30000)
    return {"min": min_salary, "max": max_salary, "currency": "USD"}

def random_url():
    return f"https://{random_string(10)}.com"

def random_phone():
    return f"({random.randint(100, 999)}) {random.randint(100, 999)}-{random.randint(1000, 9999)}"

def random_address():
    streets = ['Main St', 'Highland Ave', 'Maple St', 'Oak St']
    cities = ['San Francisco', 'Los Angeles', 'San Jose', 'San Diego']
    states = randon_state()
    return f"{random.randint(100, 9999)} {random.choice(streets)}, {random.choice(cities)}, {states}"

def random_tags():
    tags = ['AI', 'Machine Learning', 'Blockchain', 'Cloud Computing', 'DevOps', 
            'Big Data', 'Cybersecurity', 'IoT', '5G', 'Quantum Computing']
    return random.sample(tags, random.randint(1, 5))

def random_ind():
    industries = ['Technology', 'Finance', 'Healthcare', 'Retail', 'Manufacturing', 'Education', 'Transportation', 'Hospitality', 'Real Estate', 'Construction']
    return random.choice(industries)

