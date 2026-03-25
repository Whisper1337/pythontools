from __future__ import annotations

from typing import Dict, List, Optional, Tuple


Ticket = Dict[str, object]


tickets: List[Ticket] = [
    {"id": 101, "title": "VPN drops", "severity": 4, "status": "open", "owner": ""},
    {"id": 102, "title": "Password reset", "severity": 1, "status": "open", "owner": ""},
    {"id": 103, "title": "Phishing reported", "severity": 5, "status": "open", "owner": ""},
    {"id": 104, "title": "Printer offline", "severity": 2, "status": "closed", "owner": "Alex"},
    {"id": 105, "title": "Slow Wi-Fi", "severity": 3, "status": "open", "owner": ""},
]

techs = ["Alex", "Blair", "Casey"]


def severity_label(sev: int) -> str:
    """Return a human label for severity."""
    #replaced overlapping independent "if statements" with an if/elif chain
    #no more accidentl overwrights 
    if sev <= 0:
        return "Invalid"
    elif sev >= 5:
        return "High"
    elif sev >= 3:
        return "Medium"
    else:
        return "Low"


def assign_owners(tickets_list: List[Ticket], tech_list: List[str]) -> None:
    "Assign owners to open tickets in round-robin style."
    #modulo indexing makes way more snese so I removed repeated i==0/i==1/i==2 branches
    
    tech_index = 0

    for t in tickets_list:
        if t.get("status") != "open" or t.get("owner"):
            #I removed emoved useless else/pass by using an early "continue"
            continue

        t["owner"] = tech_list[tech_index]
        tech_index = (tech_index + 1) % len(tech_list)


def find_ticket_by_id(tickets_list: List[Ticket], ticket_id: int) -> Optional[Ticket]:
    """Return the ticket dict or None."""
    #return right away when it is found (basically it stops scanning)
    for t in tickets_list:
        if t.get("id") == ticket_id:
            return t
    return None


def count_by_status(tickets_list: List[Ticket]) -> Tuple[int, int]:
    """Count open and closed tickets."""
    open_count = 0
    closed_count = 0

    #using if/elif makes sure that each ticket will contributes to exactly one counter
    for t in tickets_list:
        if t.get("status") == "open":
            open_count += 1
        elif t.get("status") == "closed":
            closed_count += 1

    return open_count, closed_count


def _format_ticket_line(t: Ticket) -> str:
    """One consistent printable line for a ticket."""
    return (
        f'#{t["id"]} {t["title"]} '
        f'[{severity_label(int(t["severity"]))}] '
        f'({t["status"]}) owner={t["owner"]}'
    )


def daily_summary(tickets_list: List[Ticket]) -> None:
    "Print a summary for all tickets."
    print("=== DAILY SUMMARY ===")

    #I fixed and replaced 5 separate len() checks with one loop
    # this allows it to support as many tickets as you could possibly imagine
    for t in tickets_list:
        print(_format_ticket_line(t))

    print("=====================")


def report(tickets_list: List[Ticket]) -> None:
    "Print a report with counts and a list of open tickets."
    open_count, closed_count = count_by_status(tickets_list)
    print("=== REPORT ===")
    print("Open:", open_count)
    print("Closed:", closed_count)

    print("Open tickets:")

    #this removes the nested blocks and useless else/pass
    for t in (tk for tk in tickets_list if tk.get("status") == "open"):
        urgent_tag = " (URGENT)" if int(t["severity"]) >= 4 else ""
        print(f' - #{t["id"]}{urgent_tag} {t["title"]} owner={t["owner"]}')


def main() -> None:
    
    assign_owners(tickets, techs)

    
    daily_summary(tickets)

    
    t = find_ticket_by_id(tickets, 103) #this is the search example
    if t is not None:
        print("Found ticket:", t["title"], "severity:", severity_label(int(t["severity"])))
    else:
        print("Ticket not found")

    
    report(tickets)


if __name__ == "__main__":
    main()

