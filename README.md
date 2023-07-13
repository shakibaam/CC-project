# Project Title

The project aims to work with Docker and Kubernetes in a proper manner. We intend to containerize a relatively simple project using Docker and deploy it on Kubernetes.

## Introduction

The main objective of this project is to develop a server application that allows users to enter their desired text and obtain a unique address for accessing the note. The server communicates with a database to store the notes and their unique addresses. However, it's important to note that the stored addresses have expiration dates and are not permanently accessible.

The project is designed to be configurable, and the following fields can be customized through a configuration file:

- Port number on which the server runs
- Expiration duration of the addresses
- Database server address
- Database credentials (username and password)

By configuring these fields, users can adapt the project to their specific requirements.

## Development Server

In the development server phase, we will create a private note-taking application. Users can input their desired text, and the server will provide them with a unique address to access their note. The server is connected to a database where the notes and their unique addresses are stored.

## Dockerization

In the Dockerization step, we will write a Dockerfile that enables containerizing the project, making it portable and easily deployable across different environments.

## Kubernetes Deployment

In the Kubernetes Deployment phase, we will write the necessary deployment files to deploy the project on a Minikube cluster. This includes the configuration maps, secrets, persistent volumes, and services required for the deployment. The project will be replicated with two replicas to ensure high availability.

