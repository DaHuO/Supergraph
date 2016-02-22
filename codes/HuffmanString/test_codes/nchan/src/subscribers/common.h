ngx_int_t nchan_subscriber_subscribe(subscriber_t *sub, ngx_str_t *ch_id);

ngx_int_t nchan_subscriber_authorize_subscribe(subscriber_t *sub, ngx_str_t *ch_id);

ngx_int_t nchan_cleverly_output_headers_only_for_later_response(ngx_http_request_t *r);

ngx_str_t *nchan_request_multipart_boundary(ngx_http_request_t *r, nchan_request_ctx_t *ctx);

ngx_int_t nchan_request_set_content_type_multipart_boundary_header(ngx_http_request_t *r, nchan_request_ctx_t *ctx);