FROM node:12.18
WORKDIR ~/Desktop/s03p31a504/frontend

COPY package.json .

ADD . .
RUN npm install
EXPOSE 3000
CMD ["npm", "run", "serve"]

