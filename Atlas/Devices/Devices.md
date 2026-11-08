---
type: index
aliases: [Device Registry]
tags: [device, naming, moc]
---

# Device Registry

Devices are named after games. The rule is one franchise per domain, so a name tells you what kind of device it is:

| Franchise | Domain |
|---|---|
| Starfield | Apple ecosystem / personal computing |
| Metal Gear Solid | Audio and music gear |
| Resident Evil | Storage, backups, archives |
| The Last of Us II | Household / shared infrastructure |

Within a franchise: characters for things you carry, locations for things that sit still, ships for portable computers, corporations for anything industrial.

**Reserved:** `Constellation` is the app name and is never a device name.

## All devices

```dataview
TABLE assigned-name AS "Name", device-type AS "Device", franchise AS "Franchise", status AS "Status"
FROM "Atlas/Devices"
WHERE type = "device"
SORT placement ASC, assigned-name ASC
```

## Needs attention

```dataview
TABLE device-type AS "Device", status AS "Status"
FROM "Atlas/Devices"
WHERE type = "device" AND (status = "rename-pending" OR status = "needs-name")
SORT status ASC
```

## By placement

```dataview
TABLE rows.assigned-name AS "Names"
FROM "Atlas/Devices"
WHERE type = "device"
GROUP BY placement
```

## Household account only

```dataview
TABLE assigned-name AS "Name", device-type AS "Device"
FROM "Atlas/Devices"
WHERE type = "device" AND account = "household"
```

See [[Name Pool]] for unassigned names.
