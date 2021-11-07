# build-stage

FROM node:lts as build-stage

WORKDIR /app

COPY package.json ./

COPY yarn.lock ./

RUN yarn

COPY . .

RUN yarn build

# roduction-stage

FROM nginx:latest as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html
