# AI-Powered Interview Question Generator

## Objective

This project aims to develop an AI-powered system that automatically generates sample questions from the RS Aggarwal book for candidate screening during interviews. The system is designed to streamline the interview preparation process and enhance the quality and consistency of candidate evaluation.

## Technologies Used

- **Azure Tables**: For storing and managing generated questions
- **Few-shot prompting**: To guide the AI in generating relevant and diverse questions
- **OpenAI API**: Used for the question generation process
- **Azure Cognitive Services Speech-to-Text**: Implemented for live speech recognition functionality

## Methodology

1. **Content Analysis**: The system analyzes the content of the RS Aggarwal book, focusing on key topics, concepts, and problem-solving techniques.

2. **Few-shot Prompting**: Implements few-shot prompting to guide the AI in generating questions that match the style, difficulty, and relevance of the source material.

3. **Question Generation**: Using the analyzed content and few-shot prompts, the AI generates a diverse set of questions suitable for interview screening.

4. **Data Storage**: Azure Tables are utilized to store and manage the generated questions efficiently.

## Features

- Automated generation of interview questions based on RS Aggarwal book content
- Diverse question types and difficulty levels
- Efficient storage and retrieval of questions using Azure Tables
- Live speech-to-text functionality for dynamic interaction

## Contributing

Contributions to this project are welcome. Please feel free to submit a Pull Request or open an Issue.
