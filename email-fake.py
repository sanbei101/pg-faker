from utils import set_and_sort, format_array_sql
from consts import first_names, last_names

email_domains = [
    'qq.com', '163.com', '126.com', 'gmail.com', 'outlook.com', 'hotmail.com',
    'yahoo.com', 'sina.com', 'sohu.com', 'foxmail.com', '188.com', '139.com',
    'yeah.net', 'aliyun.com', 'vip.qq.com', 'vip.163.com', 'vip.126.com',
    'msn.com', 'live.com', 'icloud.com', 'me.com', 'protonmail.com', 'tutanota.com',
    'mail.com', 'gmx.com', 'yandex.com', 'zoho.com', 'hushmail.com', 'fastmail.com'
]

words = [
    'admin', 'user', 'manager', 'support', 'service', 'info', 'contact', 'hello', 'welcome',
    'happy', 'lucky', 'sweet', 'cool', 'smart', 'great', 'best', 'good', 'nice', 'fun',
    'star', 'sun', 'moon', 'sky', 'blue', 'green', 'red', 'gold', 'silver', 'dark',
    'light', 'bright', 'shiny', 'clear', 'pure', 'fresh', 'new', 'young', 'old', 'wise',
    'fast', 'quick', 'slow', 'steady', 'strong', 'brave', 'calm', 'quiet', 'loud', 'soft',
    'hard', 'easy', 'simple', 'complex', 'smart', 'clever', 'wise', 'kind', 'nice', 'good',
    'tech', 'data', 'code', 'web', 'net', 'app', 'dev', 'pro', 'expert', 'master',
    'student', 'teacher', 'friend', 'lover', 'hero', 'star', 'king', 'queen', 'prince', 'princess'
]

numbers = [f"{i:03d}" for i in range(1, 1001)]

separators = ['.', '_', '-']

first_names = set_and_sort(first_names)
last_names = set_and_sort(last_names)
email_domains = set_and_sort(email_domains)
words = set_and_sort(words)
numbers = set_and_sort(numbers)
separators = set_and_sort(separators)

sql = f"""-- fake邮箱地址(Python 自动生成)
CREATE OR REPLACE FUNCTION email()
RETURNS TEXT AS $$
DECLARE
    first_names TEXT[] := {format_array_sql(first_names)};
    last_names TEXT[] := {format_array_sql(last_names)};
    email_domains TEXT[] := {format_array_sql(email_domains)};
    words TEXT[] := {format_array_sql(words)};
    numbers TEXT[] := {format_array_sql(numbers)};
    separators TEXT[] := {format_array_sql(separators)};

    parts TEXT[];
    username TEXT;
    domain TEXT;
BEGIN
    parts := ARRAY[
        first_names[1 + floor(random() * array_length(first_names, 1))::int],
        last_names[1 + floor(random() * array_length(last_names, 1))::int],
        words[1 + floor(random() * array_length(words, 1))::int],
        numbers[1 + floor(random() * array_length(numbers, 1))::int]
    ];
    
    username := parts[1 + floor(random() * 4)::int] || 
                separators[1 + floor(random() * array_length(separators, 1))::int] ||
                parts[1 + floor(random() * 4)::int];
    
    domain := email_domains[1 + floor(random() * array_length(email_domains, 1))::int];

    RETURN lower(username) || '@' || domain;
END;
$$ LANGUAGE plpgsql;
"""

with open("dist/email-fake.sql", "w") as f:
    f.write(sql)

with open("dist/email-fake.sql", "w") as f:
    f.write(sql)