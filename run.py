
from cffi import FFI
ffi = FFI()

ffi.cdef("""
   void cleanup(struct cypher_parse_result_t *s);

   char * libcypher_parser_version();
   struct cypher_parse_result_t *run(const char *s);
   int cypher_parse_result_nerrors(struct cypher_parse_result_t *s);

   struct cypher_parse_error_t *cypher_parse_result_error(const struct cypher_parse_result_t *result, unsigned int index);
   char *cypher_parse_error_message(const struct cypher_parse_error_t *error);
""")

lib = ffi.dlopen("libparse.so")

def print_errors(q):
    x = lib.run(q)
    num_errors = lib.cypher_parse_result_nerrors(x)
    print "Number of errors: %s" % (num_errors, )
    for i in xrange(num_errors):
        e = ffi.string(lib.cypher_parse_error_message(lib.cypher_parse_result_error(x, i)))
        print "Message (%s): %s" % (i+1, e)

    lib.cleanup(x)

def main():
    x = lib.libcypher_parser_version()
    print "Version: %s" % (ffi.string(x), )

    print
    print_errors("MATCH (n) RET n;")
    print
    print_errors("MATCH (n) RETURN n;")


if __name__ == '__main__':
    main()

