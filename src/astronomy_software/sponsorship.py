import requests
import os

def get_open_collective_info(slug):
    """
    Fetches basic information about a collective from Open Collective.
    """
    url = "https://api.opencollective.com/graphql/v2"
    query = """
    query collective($slug: String) {
      collective(slug: $slug) {
        name
        description
        website
        stats {
          balance {
            value
            currency
          }
          backers {
            all
          }
        }
      }
    }
    """
    variables = {"slug": slug}
    try:
        response = requests.post(url, json={"query": query, "variables": variables})
        if response.status_code == 200:
            return response.json().get("data", {}).get("collective")
    except Exception as e:
        print(f"Error fetching Open Collective info: {e}")
    return None

def get_patreon_info():
    """
    Fetches basic information from Patreon.
    Requires PATREON_ACCESS_TOKEN environment variable.
    """
    access_token = os.environ.get("PATREON_ACCESS_TOKEN")
    if not access_token:
        return None

    url = "https://www.patreon.com/api/oauth2/v2/campaigns"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        print(f"Error fetching Patreon info: {e}")
    return None
