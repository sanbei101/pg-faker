FROM alpine:latest AS downloader

ARG DOWNLOAD_URL=https://github.com/PostgREST/postgrest/releases/download/v14.0/postgrest-v14.0-linux-static-x86-64.tar.xz

RUN apk add --no-cache wget xz

RUN wget -O /tmp/postgrest.tar.xz "${DOWNLOAD_URL}" && \
    tar -xf /tmp/postgrest.tar.xz -C /tmp/ && \
    rm /tmp/postgrest.tar.xz

FROM gcr.io/distroless/static-debian12:nonroot

COPY --from=downloader /tmp/postgrest /postgrest
COPY postgrest.conf /postgrest.conf

EXPOSE 3000
ENTRYPOINT ["/postgrest"]
CMD ["/postgrest.conf"]