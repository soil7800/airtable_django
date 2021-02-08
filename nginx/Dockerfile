FROM node:latest as build-stage
WORKDIR /app-frontend
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
RUN npm install
COPY ./frontend/ .
RUN npm run build

FROM nginx as production-stage
RUN mkdir /app-frontend
COPY --from=build-stage /app-frontend/dist /app-frontend
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d
ENV LISTEN_PORT=80
EXPOSE 80
