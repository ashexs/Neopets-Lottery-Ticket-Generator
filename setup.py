from setuptools import setup, find_packages

setup(
    name='lottery-ticket-generator',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'lottery-ticket-generator=lottery_ticket_generator.main:main'
        ]
    }
)
