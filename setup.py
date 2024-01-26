from setuptools import setup, find_packages

# 패키지 이름
name = "django-tagify-widget"

# 패키지 버전
version = "0.1.1"

# 패키지 설명
description = "Django widgets with tagify.js"

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

# 패키지 URL (옵션)
url = "https://github.com/zzqyu/django-tagify-widget"

# 저자 정보
author = "zzqyu"
author_email = "wjdrb0626@naver.com"

# 패키지 라이센스
license = "MIT"

# 패키지 종속성 (다른 패키지에 대한 정보, 필요한 경우 추가)
install_requires = [
    'Django>=2.0.0',
]

# 패키지 정보
setup(
    name=name,
    version=version,
    description=description,
    long_description = long_description,
    long_description_content_type='text/markdown',
    url=url,
    author=author,
    author_email=author_email,
    license=license,
    packages=find_packages(include=['tagify_widget']),
    install_requires=install_requires,
    python_requires='>=3',
    platforms=['Any'],
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
)