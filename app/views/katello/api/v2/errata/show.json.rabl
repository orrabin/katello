object @resource

attributes :uuid => :id
attributes :title, :errata_id
attributes :issued, :updated, :version, :status, :release
attributes :severity, :description, :solution, :summary, :reboot_suggested
attributes :_href
attributes :cves

attributes :errata_type => :type

node(:systems_available_count) { |m| m.systems_available.count }

node :packages do |e|
  e.packages.pluck(:nvrea)
end
