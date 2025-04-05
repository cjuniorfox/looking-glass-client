# Looking Glass Client for COPR

This repository means to be used as the placeholder for the Fedora's Looking Glass Client builder.

## Compiling by yourself

1. Download the sources

  ```bash
    spectool -g -R looking-glass-client.spec
  ```

2. Compile

  ```bash
    rpmbuild -ba looking-glass-client.spec
  ```
