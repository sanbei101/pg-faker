FROM alpine:latest as downloader
ARG DOWNLOAD_URL= https://github.com/PostgREST/postgrest/releases/download/v14.0/postgrest-v14.0-linux-static-x86-64.tar.xz
ADD ${DOWNLOAD_URL} /tmp/

RUN tar -xf /tmp/postgrest-v14.0-linux-static-x86-64.tar.xz -C /tmp/

FROM gcr.io/distroless/static-debian12:nonroot

COPY --from=downloader /tmp/postgrest /postgrest

COPY postgrest.conf /postgrest.conf

EXPOSE 3000
ENTRYPOINT ["/postgrest"]
CMD ["/postgrest.conf"]