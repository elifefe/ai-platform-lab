terraform {
  required_providers {
    render = {
      source  = "render-oss/render"
      version = "~> 1.9"
    }
  }
}

provider "render" {}

resource "render_web_service" "ai_platform_lab" {
  name   = "ai-platform-lab"
  plan   = "free"
  region = "oregon"
  runtime_source = {
    docker = {
      repo_url    = "https://github.com/elifefe/ai-platform-lab"
      branch      = "main"
      auto_deploy = true
    }
  }
}