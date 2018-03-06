# EC2 Deploy project

AWS의 EC2 배포를 연습하는 프로젝트입니다.
'.secrets'폴더 파일로 비밀 키를 관리합니다.

## requirements

- Python (3.6)
- PostgreSQL

## Installation

```
pip install -r requirements.txt
```

## Secrets

**`.secrets/base.json`**

```json
{
   "SECRET_KEY":"<Django settings SECRET_KEY value>""
}
```

**`.secrets/local.json`**


```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "localhost",
      "NAME": "ec2_deploy",
      "USER": "kahee",
      "PASSWORD": "rkgml12345",
      "POST": 5432
    }
  }
}

```

**`.secrets/dev.json`**
> PostgreSQL(AWS RDS)을 사용한다.

```json
{
  "DATABASES": {
    "default": {
      "ENGINE": "django.db.backends.postgresql",
      "HOST": "<자신의 RDS주소, ex) instance-name.###.regin.rds.amazonaws.com",
      "NAME": "ec2_deploy",
      "USER": "kahee",
      "PASSWORD": "rkgml12345",
      "POST": 5432
    }
  }
}

```