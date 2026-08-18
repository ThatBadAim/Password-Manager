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
                    "Pencil" => "\uE70F", // Edit icon
                    "Eye" => "\uE890", // View icon
                    "Copy" => "\uE8C8", // Copy icon
                    "Plus" => "\uE710", // Add icon
                    "Shield" => "\uEA18", // Shield icon
                    "Calendar" => "\uE787", // Calendar icon
                    "History" => "\uE81C", // History icon
                    _ => "\uE783" // Default fallback icon
                };
            }
            return "\uE783";
        }

        public object ConvertBack(object value, Type targetType, object parameter, CultureInfo culture)
        {
            throw new NotImplementedException();
        }
    }
}
