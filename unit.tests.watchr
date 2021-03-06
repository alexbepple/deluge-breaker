#!/usr/bin/env ruby

def nose(tests)
    system("./bin/python /usr/local/bin/nosetests --with-color #{tests}")
end

def run_all_unit_tests()
    nose("tests/unit")
end

watch('.*\.py') {run_all_unit_tests()}
