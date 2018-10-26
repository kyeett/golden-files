# Golden-files

Simple example application in Python using golden files for testing.

## Usage

Run example application

```bash
╰─$ python example.py
```

Run tests

```bash
╰─$ python -m pytest
```

### Updating .golden files

If you have done changes to the functions, you need to refresh the .golden files, as expected output is different. In this example, I changed the indentation level.

```bash
╰─$ python example.py --update
updating golden files
```

```bash
╰─$ git diff
...
-    {
-        "first_name": "Jeanette",
-        "last_name": "PENDDRETH",
-        "email": "jpenddreth0@census.gov",
-        "location": "Unknown",
-        "ip_address": "26.58.193.2",
-        "id": 0
-    }
+{
+"first_name": "Jeanette",
+"last_name": "PENDDRETH",
+"email": "jpenddreth0@census.gov",
+"location": "Unknown",
+"ip_address": "26.58.193.2",
+"id": 0
+}
```

Run the test. If the framework is correctly written, it should always pass after using the --update flag.

```bash
╰─$ python -m pytest
```

## Todo

1. ~~Create golden files~~
2. ~~Create test using golden files~~
3. ~~Refresh data with flag~~
4. ~~Update documentation~~
5. Run application using golden files (for part if it?)