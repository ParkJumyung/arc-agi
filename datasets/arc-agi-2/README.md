# ARC-AGI-2 Dataset

## Summary

The original ARC-AGI-2 Dataset from [ARC Prize](https://arcprize.org).

## Source

[ARC-Prize ARC-AGI-2 Repository (commit hash: 1ef37bc)](https://github.com/arcprize/ARC-AGI-2/tree/1ef37bc909c180481ed6827da2d34793353e2f54)

## License

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Directory Structure

```
.
├── training: training tasks (# 1000)
├── evaluation: public evaluation tasks (# 120)
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
