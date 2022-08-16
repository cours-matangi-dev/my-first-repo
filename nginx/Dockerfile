FROM nginx:1.21.6-alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx/nginx.conf /etc/nginx/conf.d
RUN addgroup --system --gid 101 nginx
RUN adduser --system --disabled-login --ingroup nginx --uid 101 -D nginx 
USER user
CMD ["nginx", "-g", "daemon off;"]
