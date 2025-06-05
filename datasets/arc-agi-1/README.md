# ARC-AGI-1 Dataset

## Summary

The original ARC-AGI-1 Dataset from [François Chollet](https://fchollet.com).

## Source

[François Chollet Repository (commit hash: 3990304)](https://github.com/fchollet/ARC-AGI/tree/399030444e0ab0cc8b4e199870fb20b863846f34)

## License

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Directory Structure

```
.
├── training: training tasks (# 400)
├── evaluation: public evaluation tasks (# 400)
└── task.schema.json: JSON schema of
```

## Task Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "train": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "input": {
            "type": "array",
            "minItems": 1,
            "maxItems": 30,
            "items": {
              "type": "array",
              "minItems": 1,
              "maxItems": 30,
              "items": {
                "type": "integer",
                "minimum": 0,
                "maximum": 9
              }
            }
          },
          "output": {
            "type": "array",
            "minItems": 1,
            "maxItems": 30,
            "items": {
              "type": "array",
              "minItems": 1,
              "maxItems": 30,
              "items": {
                "type": "integer",
                "minimum": 0,
                "maximum": 9
              }
            }
          }
        },
        "required": ["input", "output"]
      }
    },
    "test": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "input": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            }
          },
          "output": {
            "type": "array",
            "items": {
              "type": "array",
              "items": {
                "type": "integer"
              }
            }
          }
        },
        "required": ["input", "output"]
      }
    }
  },
  "required": ["train", "test"]
}
```
