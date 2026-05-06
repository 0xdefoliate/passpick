# passpick

A boring utility for generating passwords & passphrases, forked and improved substantially over the upstream.  
I decided to improve upon the source mostly out of boredom.

## Building

1. Clone the repo via `git`
2. Create a `venv` and enter into it
3. Install dependencies via `pip`
4. Run `python3 -m build`
5. Bob's your uncle

## Examples

```bash
# Generate an 8-word long passphrase
$ passpick -pL 8

# Generate a 64-character (default) long password
$ passpick
```
