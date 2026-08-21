using System;
using System.Globalization;
using System.Windows.Data;

namespace CipherVault.Converters
{
    public class IconConverter : IValueConverter
    {
        public object Convert(object value, Type targetType, object parameter, CultureInfo culture)
        {
            if (value is string iconName)
            {
                return iconName switch
                {
                    "Search" => "\uE1A3",
                    "Sync" => "\uE895",
                    "Help" => "\uE897",
                    "Profile" => "\uE77B",
                    "Copy" => "\uE8C8",
                    "Eye" => "\uE18B",
                    "Pencil" => "\uE104",
                    "External" => "\uE8A7",
                    "Shield" => "\uEA18",
                    "Calendar" => "\uE787",
                    "History" => "\uE81C",
                    "Plus" => "\uE710",
                    _ => string.Empty
                };
            }
            return string.Empty;
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
