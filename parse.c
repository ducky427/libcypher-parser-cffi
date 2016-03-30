#include <cypher-parser.h>
#include <errno.h>
#include <stdio.h>

void cleanup(cypher_parse_result_t *result)
{
    cypher_parse_result_free(result);
}

cypher_parse_result_t *run(const char * s)
{
    cypher_parse_result_t *result = cypher_parse(s, NULL, NULL, CYPHER_PARSE_ONLY_STATEMENTS);
    return result;
}

int main(int argc, char *argv[])
{
    cypher_parse_result_t *result = cypher_parse(
            "MATCH (n) RETURN n", NULL, NULL, CYPHER_PARSE_ONLY_STATEMENTS);
    if (result == NULL)
    {
        perror("cypher_parse");
        return EXIT_FAILURE;
    }
    printf("Parsed %d AST nodes\n", cypher_parse_result_node_count(result));
    cypher_parse_result_free(result);
    return 0;
}
