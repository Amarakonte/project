# Utilisez une image de base Go avec Alpine Linux
FROM golang:1.16-alpine

# Créez un répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers nécessaires dans le conteneur
COPY assets/ /app/assets
COPY config/ /app/config
COPY cookies/ /app/cookies
COPY main.go .
COPY public/ /app/public
COPY vendor/ /app/vendor
COPY go.mod .
COPY go.sum .

# Déplacez-vous dans le répertoire "main" de votre projet
WORKDIR /app

# Compilez votre application Go
RUN go build -o main

# Exposez le port sur lequel votre application écoute
EXPOSE 8000

# Exécutez votre application lorsque le conteneur démarre
CMD ["./main", "-p", "$PORT"]
