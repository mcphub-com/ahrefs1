import requests
from datetime import datetime
from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")
from pydantic import BaseModel, Field
from typing import Union
from typing import Annotated

mcp = FastMCP('ahrefs1')

@mcp.tool()
def keyword_difficulty_checker(keyword: Annotated[str, Field(description="Keyword")],
                               country: Annotated[str, Field(description="Country code")] = None) -> dict: 
    '''Find out how hard it'll be to rank in the top 10 for any keyword.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/keyword-difficulty-checker'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'country': country,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def google_keyword_generator(keyword: Annotated[str, Field(description="Keyword")],
                             country: Annotated[str, Field(description="Country code")] = None) -> dict: 
    '''Find thousands of relevant keyword ideas in seconds.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/keyword-generator/google'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'country': country,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def bing_keyword_generator(keyword: Annotated[str, Field(description="Keyword")],
                           country: Annotated[str, Field(description="Country code")] = None) -> dict: 
    '''Discover the keywords people search for on Bing. Analyze their SEO potential.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/keyword-generator/bing'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'country': country,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def you_tube_keyword_generator(keyword: Annotated[str, Field(description="Keyword")],
                               country: Annotated[str, Field(description="Country code")] = None) -> dict: 
    '''Get more views on YouTube by researching keywords people are searching for.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/keyword-generator/youtube'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'country': country,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def amazon_keyword_generator(keyword: Annotated[str, Field(description="Keyword")],
                             country: Annotated[str, Field(description="Country code")] = None) -> dict: 
    '''Find what people are searching for on Amazon, and align your product listings with those terms.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/keyword-generator/amazon'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'country': country,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def backlink_checker(url: Annotated[str, Field(description="Target URL")],
                     mode: Annotated[str, Field(description="One of the following:")] = None) -> dict: 
    '''See the top 100 backlinks to any website or webpage.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/backlink-checker'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'mode': mode,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def website_authority_checker(url: Annotated[str, Field(description="Target URL")]) -> dict: 
    '''Check the Domain Rating (DR) of any website to see the strength of its backlink profile.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/website-authority-checker'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def broken_link_checker(url: Annotated[str, Field(description="Target URL")],
                        mode: Annotated[str, Field(description="One of the following:")] = None) -> dict: 
    '''Find broken links to and from any webpage or website in seconds.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/broken-link-checker'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'mode': mode,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def website_traffic_checker(url: Annotated[str, Field(description="Target URL")],
                            mode: Annotated[str, Field(description="One of the following:")] = None) -> dict: 
    '''See search traffic estimates for any website or webpage.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/website-traffic-checker'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'url': url,
        'mode': mode,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def keyword_rank_checker(keyword: Annotated[str, Field(description="Keyword")],
                         domain: Annotated[str, Field(description="Target domain")],
                         country: Annotated[str, Field(description="Country code")] = None) -> dict: 
    '''Check your site's ranking position in any country.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/keyword-rank-checker'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'domain': domain,
        'country': country,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

@mcp.tool()
def serpchecker(keyword: Annotated[str, Field(description="Keyword")],
                country: Annotated[str, Field(description="Country code")] = None) -> dict: 
    '''Analyze the top 10 rankings for any keyword in any country.'''
    url = 'https://ahrefs1.p.rapidapi.com/v1/serp-checker'
    headers = {'x-rapidapi-host': 'ahrefs1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'keyword': keyword,
        'country': country,
    }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code != 200:
        return {}
    return response.json()

if __name__ == "__main__":
    mcp.run(transport="stdio")