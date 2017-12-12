gen:
	docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
		-i /local/swagger.yaml \
		-l python \
		-o /local/ -c /local/swagger_py.json
